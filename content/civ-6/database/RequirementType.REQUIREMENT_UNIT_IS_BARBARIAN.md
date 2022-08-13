---
tags:
- RequirementType
title: REQUIREMENT_UNIT_IS_BARBARIAN
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_UNIT_IS_BARBARIAN
>
> * Class: `UNITS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_UNIT_NOT_BARBARIAN"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"REQUIRES_UNIT_NOT_BARBARIAN",
		"REQUIREMENT_UNIT_IS_BARBARIAN",
		1
	);


```
