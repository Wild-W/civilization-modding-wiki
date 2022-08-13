---
tags:
- RequirementType
title: REQUIREMENT_TOURISTS_EXCEED_STAYCATIONERS
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_TOURISTS_EXCEED_STAYCATIONERS
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="CULTURE_VICTORY_ENOUGH_TOURISTS_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"CULTURE_VICTORY_ENOUGH_TOURISTS_REQUIREMENT",
		"REQUIREMENT_TOURISTS_EXCEED_STAYCATIONERS"
	);

```
