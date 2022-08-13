---
tags:
- RequirementType
title: REQUIREMENT_UNIT_IN_OWNER_TERRITORY
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_UNIT_IN_OWNER_TERRITORY
>
> * Class: `UNITS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_UNIT_NOT_IN_OWNER_TERRITORY"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"REQUIRES_UNIT_NOT_IN_OWNER_TERRITORY",
		"REQUIREMENT_UNIT_IN_OWNER_TERRITORY",
		1
	);


```
