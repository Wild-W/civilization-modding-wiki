---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_QUEEN_OF_NILE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_QUEEN_OF_NILE
>
> * Class: `PLAYERS`
> * Parameters:
>	* StatementKey `String`

## Samples
```SQL {title="AGENDA_QUEEN_OF_NILE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_QUEEN_OF_NILE",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_QUEEN_OF_NILE",
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
		"AGENDA_QUEEN_OF_NILE",
		"StatementKey",
		"AGENDA_QUEEN_OF_NILE_WARNING"
	);
	
```

