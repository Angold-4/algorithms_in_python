using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rope : MonoBehaviour
{
    // Start is called before the first frame update
    
    public GameObject ropeSegmentPrefab;

    List<GameObject> ropeSegments = new List<GameObject>();

    public bool isIncreasing {get; set;}
    public bool isDecreasing {get; set;}

    public Rigidbody2D connectedObject;
    public float maxRopeSegmentLength = 1.0f;
    public float ropeSpeed = 4.0f;

    LineRenderer lineRenderer;
    void Start()
    {
        lineRenderer = GetComponent<LineRenderer>();
        ResetLength();
        
    }

    public void ResetLength(){
        foreach (GameObject segment in ropeSegments){
            Destroy (segment);
        }

        ropeSegments = new List<GameObject>();

        isDecreasing = false;
        isIncreasing = false;

        CreateRopeSegment();

    }

    void CreateRopeSegment(){
        //Create New Segment to Obtain to the man or another segment
        GameObject segment = (GameObject)Instantiate(
        ropeSegmentPrefab,
        this.transform.position,
        Quaternion.identity);

        segment.transform.SetParent(this.transform, true);

        Rigidbody2D segmentBody = segment.GetComponent<Rigidbody2D>();
        SpringJoint2D segmentJoint = segment.GetComponent<SpringJoint2D>();

        if (segmentJoint == null || segmentBody == null){
            Debug.LogError("Rope segment body prefab has no" + "Rigidbody2D and/or SpringJoint2D!");
            return;
        }
        ropeSegments.Insert(0, segment);

        //If it is the first segment. It need to connect the connectedObject(Man)

        if (ropeSegments.Count == 1){
            SpringJoint2D connectedObjectJoint = connectedObject.GetComponent<SpringJoint2D>();
            connectedObjectJoint.connectedBody = segmentBody;
            connectedObjectJoint.distance = 0.1f;
        }else{//It is not the first segment. So It need to connect to the segmentJoint(Also As SegmentJoint)
            GameObject nextSegment = ropeSegments[1];//Obtain the Second Segmen;
            SpringJoint2D nextSegmentJoint = nextSegment.GetComponent<SpringJoint2D>();

            nextSegmentJoint.connectedBody = segmentBody;

            segmentJoint.distance = 0.0f;
        }
            //Obtain this segmentjoint
            segmentJoint.connectedBody = this.GetComponent<Rigidbody2D>();
    }

    void RemoveRopeSegment(){
        //If it don't have more than 1 segments. Stop Remove
        if (ropeSegments.Count < 2){
            return;
        }

        GameObject topSegment = ropeSegments[0];
        GameObject nextSegment = ropeSegments[1];

        SpringJoint2D nextSegmentJoint = nextSegment.GetComponent<SpringJoint2D>();
        nextSegmentJoint.connectedBody = this.GetComponent<Rigidbody2D>();

        //Remove the top segment
        ropeSegments.RemoveAt(0);
        Destroy(topSegment);
    }



    // Update is called once per frame
    void Update()
    {
        //Get the top rope segment and segmentjoint
        GameObject topSegment = ropeSegments[0];
        SpringJoint2D topSegmentJoint = topSegment.GetComponent<SpringJoint2D>();

        if (isIncreasing){
            //If the length of the rope has reached the maximum length, then add a new rope segment
            if (topSegmentJoint.distance >= maxRopeSegmentLength){
                CreateRopeSegment();
            }else{
                topSegmentJoint.distance += ropeSpeed * Time.deltaTime;
            }
        }

        if (isDecreasing){
            //Shorten the rope if its length is close to 0, then delete this rope segment
            if (topSegmentJoint.distance <= 0.005f){
                RemoveRopeSegment();
            }else{
                topSegmentJoint.distance -= ropeSpeed * Time.deltaTime;
            }
        }

        //Render Line
        if (lineRenderer != null){
            lineRenderer.positionCount = ropeSegments.Count + 2;
            lineRenderer.SetPosition(0, this.transform.position);

            for (int i=0; i < ropeSegments.Count; i++){
                lineRenderer.SetPosition(i+1, ropeSegments[i].transform.position);
            }

            SpringJoint2D connectedObjectJoint = connectedObject.GetComponent<SpringJoint2D>();
            lineRenderer.SetPosition(ropeSegments.Count + 1, connectedObject.transform.TransformPoint(connectedObjectJoint.anchor));
        }
    }
}

