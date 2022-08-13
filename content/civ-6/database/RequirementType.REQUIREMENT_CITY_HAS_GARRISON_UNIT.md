---
tags:
- RequirementType
title: REQUIREMENT_CITY_HAS_GARRISON_UNIT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_HAS_GARRISON_UNIT
>
> * Class: `CITIES`
> * Arguments:
>	* MilitaryFormation `String`
>		* ARMY_MILITARY_FORMATION>		  CORPS_MILITARY_FORMATION

## Samples

```SQL {title="REQUIRES_CITY_HAS_GARRISON_UNIT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_CITY_HAS_GARRISON_UNIT",
		"REQUIREMENT_CITY_HAS_GARRISON_UNIT"
	);


```

```SQL {title="REQUIRES_CITY_HAS_GARRISON_ARMY"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_CITY_HAS_GARRISON_ARMY",
		"REQUIREMENT_CITY_HAS_GARRISON_UNIT"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_CITY_HAS_GARRISON_ARMY",
		"MilitaryFormation",
		"ARMY_MILITARY_FORMATION"
	);
	
```
