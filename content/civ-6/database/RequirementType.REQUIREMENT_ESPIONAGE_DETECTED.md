---
tags:
- RequirementType
title: REQUIREMENT_ESPIONAGE_DETECTED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_ESPIONAGE_DETECTED
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_ESPIONAGE_DETECTED"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Triggered
	)
VALUES
	(
		"REQUIRES_ESPIONAGE_DETECTED",
		"REQUIREMENT_ESPIONAGE_DETECTED",
		1
	);


```
