---
tags:
- RequirementType
title: REQUIREMENT_ALWAYS_MET
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_ALWAYS_MET
>
> * Class: `ANY`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_NOTHING"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_NOTHING",
		"REQUIREMENT_ALWAYS_MET"
	);

```
