---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_BULL_MOOSE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_BULL_MOOSE
>
> * Class: `PLAYERS`
> * Parameters:
>	* StatementKey `Unknown`

## Samples
```SQL {title="AGENDA_BULL_MOOSE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_BULL_MOOSE",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_BULL_MOOSE",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_10_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_BULL_MOOSE",
		"StatementKey",
		"LOC_PLACEHOLDER"
	);
	
```

