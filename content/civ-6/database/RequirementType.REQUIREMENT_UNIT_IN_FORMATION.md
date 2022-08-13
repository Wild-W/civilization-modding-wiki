---
tags:
- RequirementType
title: REQUIREMENT_UNIT_IN_FORMATION
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_UNIT_IN_FORMATION
>
> * Class: `UNITS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="UNIT_IS_IN_FORMATION_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"UNIT_IS_IN_FORMATION_REQUIREMENT",
		"REQUIREMENT_UNIT_IN_FORMATION"
	);


```
