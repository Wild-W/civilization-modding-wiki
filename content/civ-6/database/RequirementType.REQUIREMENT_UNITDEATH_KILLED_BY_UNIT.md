---
tags:
- RequirementType
title: REQUIREMENT_UNITDEATH_KILLED_BY_UNIT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_UNITDEATH_KILLED_BY_UNIT
>
> * Class: `Unknown`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="UNIT_KILLED_BY_UNIT_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"UNIT_KILLED_BY_UNIT_REQUIREMENT",
		"REQUIREMENT_UNITDEATH_KILLED_BY_UNIT"
	);


```
