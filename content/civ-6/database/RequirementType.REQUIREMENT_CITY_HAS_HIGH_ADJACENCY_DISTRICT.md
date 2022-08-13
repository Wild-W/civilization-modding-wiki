---
tags:
- RequirementType
title: REQUIREMENT_CITY_HAS_HIGH_ADJACENCY_DISTRICT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_HAS_HIGH_ADJACENCY_DISTRICT
>
> * Class: `CITIES`
> * Arguments:
>	* YieldType `String`
>		* [Yields.YieldType]
>	* DistrictType `String`
>		* [Districts.DistrictType]
>	* Amount `Integer`

## Samples

```SQL {title="REQUIRES_CAMPUS_HAS_HIGH_ADJACENCY"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_CAMPUS_HAS_HIGH_ADJACENCY",
		"REQUIREMENT_CITY_HAS_HIGH_ADJACENCY_DISTRICT"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_CAMPUS_HAS_HIGH_ADJACENCY",
		"Amount",
		4
	),
	(
		"REQUIRES_CAMPUS_HAS_HIGH_ADJACENCY",
		"DistrictType",
		"DISTRICT_CAMPUS"
	),
	(
		"REQUIRES_CAMPUS_HAS_HIGH_ADJACENCY",
		"YieldType",
		"YIELD_SCIENCE"
	);
	
```
